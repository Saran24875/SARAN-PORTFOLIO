from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from branding.models import PersonalBranding
from .models import ContactInfo, Client_Message
from .forms import ContactForm
# import openai  # AI Integration (Free Alternative Available)
import google.generativeai as genai
import random
import requests
from django.contrib import messages  # Import Django messages framework
from django.urls import reverse




failed_zerobounce_keys = set()  # Track failed API keys

def validate_email_with_zerobounce(email):
    """Validate email existence using multiple ZeroBounce API keys"""
    global failed_zerobounce_keys

    available_keys = [key for key in settings.ZEROBOUNCE_API_KEYS if key not in failed_zerobounce_keys]

    if not available_keys:
        print("⚠️ No working ZeroBounce API keys available. Skipping validation.")
        return True  # Assume valid if no API keys work

    for api_key in available_keys:
        url = f"https://api.zerobounce.net/v2/validate?api_key={api_key}&email={email}"

        try:
            response = requests.get(url)
            print(f"ZeroBounce API Response Status Code: {response.status_code} (Key: {api_key})")
            print(f"Response Content: {response.text}")

            if response.status_code == 404:
                print(f"⚠️ ZeroBounce API endpoint not found for key {api_key}. Skipping.")
                failed_zerobounce_keys.add(api_key)
                continue  # Try the next key

            if response.status_code != 200:
                print(f"❌ ZeroBounce returned {response.status_code} for key {api_key}. Marking as failed.")
                failed_zerobounce_keys.add(api_key)
                continue  # Try the next key

            data = response.json()
            print("ZeroBounce API Response:", data)

            if data.get("status") == "valid":
                return True  # Valid email

            return False  # Invalid email

        except requests.exceptions.RequestException as e:
            print(f"🚨 Request failed with key {api_key}: {e}")
            failed_zerobounce_keys.add(api_key)  # Mark key as failed
            continue  # Try the next key

        except ValueError as e:
            print(f"⚠️ JSON Decode Error with key {api_key}: {e}")
            failed_zerobounce_keys.add(api_key)
            continue  # Try the next key

    return True  # If all API keys fail, assume the email is valid


    
# Track failed API keys
failed_keys = set()

def get_ai_response(user_message):
    """Generate AI-based responses using multiple Gemini API keys"""
    global failed_keys

    available_keys = [key for key in settings.GEMINI_API_KEYS if key not in failed_keys]

    if not available_keys:
        return "I'm currently unable to generate a response. Please try again later."

    for api_key in available_keys:
        try:
            # Configure Gemini API with the selected key
            genai.configure(api_key=api_key)

            # Load the Gemini model
            model = genai.GenerativeModel("gemini-2.0-flash")

            # Get the first custom prompt
            contact_info = ContactInfo.objects.first()  # Get the first ContactInfo object
            custom_prompt = contact_info.ai_details if contact_info and contact_info.ai_details else (
            "You are an AI assistant for a website contact form. "
            "Please generate a helpful and professional response to the following user inquiry:\n\n"
        )

            # Default prompt if none is found
            # custom_prompt = ai_prompt.prompt_text if ai_prompt else (
            #     "You are an AI assistant for a website contact form. "
            #     "Please generate a helpful and professional response to the following user inquiry:\n\n"
            # )
            full_message = custom_prompt + user_message

                # Generate AI response
            response = model.generate_content(full_message)

            return response.text if response else "I'm unable to generate a response right now."

        except Exception as e:
            print(f"Google AI Error with API Key {api_key}: {e}")
            failed_keys.add(api_key)  # Mark this key as failed and try the next one

    return "AI response is temporarily unavailable. Please try again later."


# def get_ai_response(user_message):
#     """Generate AI-based responses using Google Gemini API"""
#     try:
#         # Configure Gemini API key
#         genai.configure(api_key=settings.GOOGLE_API_KEY)

#         # Load the Gemini model
#         model = genai.GenerativeModel("gemini-pro")


#         # Add a custom system prompt before the user message
#         custom_prompt = (
#             "You are an AI assistant for a website contact form. "
#             "Please generate a helpful and professional response to the following user inquiry:\n\n"
#         )
#         full_message = custom_prompt + user_message  # Combine both messages

#         # Generate AI response
#         response = model.generate_content(full_message)

#         # Debugging: Print response to check output
#         print(f"AI Response: {response.text}")

#         return response.text if response else "I'm unable to generate a response right now."

#     except Exception as e:
#         print(f"Google AI Error: {e}")
#         return "I'm currently unable to generate a response. Please try again later."

# def get_ai_response(user_message):
#     """Generate AI-based responses for client inquiries."""
    # try:
    #     openai.api_key = settings.OPENAI_API_KEY  # Use API key from settings
    #     response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "user", "content": user_message}]
    #     )
    #     print(f"AI Response: {response}")

    #     return response["choices"][0]["message"]["content"]
    # except openai.OpenAIError as e:
    #     print(f"OpenAI Error: {e}")  # Print any OpenAI API errors
    #     return "Sorry, I couldn't generate a response at the moment."
    # except Exception as e:
    #     print(f"Error: {e}")  # Catch any other errors
    #     return "Sorry, I couldn't generate a response at the moment."
    # except Exception as e:
    #     return "Thanks for contancting {name}, I will get back to you soon!"


def contact_page(request):
    branding = PersonalBranding.objects.first()  # Fetch first branding object
    contact = ContactInfo.objects.first()  # Fetch first ContactInfo object

    # Prepare active social media links with icons
    social_media_links = []
    if contact:
        icons = contact.get_social_media_icons()
        for platform, icon_class in icons.items():
            link = getattr(contact, platform, None)
            active = getattr(contact, f"{platform}_active", False)
            if link and active:
                social_media_links.append({
                    "platform": platform.title(),
                    "url": link,
                    "icon_class": icon_class,
                })

    # Contact Form Handling
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
                
            # Validate the email using ZeroBounce API
            if not validate_email_with_zerobounce(email):
                form.add_error("email", "This email address is does not exist.")
                return render(request, "contact.html", {
                                    "contact": contact,
                                    "social_media_links": social_media_links,
                                    "branding": branding,
                                    "form": form,  # Pass form to template
                                })
            # Continue with the rest of the logic after validation (sending emails, etc.)
            

            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # message = form.cleaned_data["message"]

            # subject = f"New Contact Form Submission from {name}"
            # email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # # Get the admin's email dynamically from ContactInfo
            # admin_email = contact.email if contact and contact.email else settings.EMAIL_HOST_USER

            # # Debugging: Print admin email
            # print(f"Admin Email: {admin_email}")
                        # Get the admin's email dynamically from ContactInfo
            admin_email = contact.email if contact and contact.email else settings.EMAIL_HOST_USER

            # Subject and body for admin email
            subject = f"You have received a new contact form submission. {name}"

            # Generate AI response using Google Gemini
            ai_reply = get_ai_response(message)
            
            Client_Message.objects.create(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            message=form.cleaned_data["message"],
            Ai_Response=ai_reply
            )

            # Construct the email message to the admin
            email_message = f"""
            New Contact Form Submission from
            
            Name: {name}
            
            Email: {email}

            --- Client's Message ---
            {message}

            --- AI Response ---
            {ai_reply}
            """

            if admin_email:
                send_mail(
                    subject,
                    email_message,
                    settings.EMAIL_HOST_USER,
                    [admin_email],
                    fail_silently=False,
                )
            else:
                print("⚠️ No admin email found! Email not sent.")

            # Generate AI response

            # Send AI-generated response to client
            send_mail(
                f"Hello {name}! Your message has been received.",
                ai_reply,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            
            messages.success(request, "✅ Your message has been sent successfully! We will get back to you soon.")

            return redirect(reverse('index') + '#contactpage')  # scrolls to contact section on the index page


    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "contact": contact,
        "social_media_links": social_media_links,
        "branding": branding,
        "form": form,  # Pass form to template
    })

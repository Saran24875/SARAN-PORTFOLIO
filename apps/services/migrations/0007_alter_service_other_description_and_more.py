# Generated by Django 5.1.7 on 2025-03-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_other_description_alter_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Other_description',
            field=models.TextField(blank=True, help_text="Provide a description for the 'Others' entry if applicable."),
        ),
        migrations.AlterField(
            model_name='service',
            name='Othericon',
            field=models.CharField(blank=True, help_text="Enter an icon for the 'Others' entry, if applicable.", max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='Others',
            field=models.CharField(blank=True, help_text='Enter a custom service name if not selecting from the list.', max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='Select_Service',
            field=models.CharField(blank=True, choices=[('Web Development', 'Web Development'), ('Frontend Development', 'Frontend Development'), ('Backend Development', 'Backend Development'), ('Full Stack Development', 'Full Stack Development'), ('App Development', 'App Development'), ('Android Development', 'Android Development'), ('iOS Development', 'iOS Development'), ('Cross-Platform Development', 'Cross-Platform Development'), ('Software Development', 'Software Development'), ('Desktop Application Development', 'Desktop Application Development'), ('Enterprise Software Development', 'Enterprise Software Development'), ('Embedded Systems Development', 'Embedded Systems Development'), ('Game Development', 'Game Development'), ('AR/VR Development', 'AR/VR Development'), ('Data Science & AI Development', 'Data Science & AI Development'), ('Machine Learning Development', 'Machine Learning Development'), ('AI Development', 'AI Development'), ('Data Analytics & Visualization', 'Data Analytics & Visualization'), ('Big Data Development', 'Big Data Development'), ('Blockchain Development', 'Blockchain Development'), ('Smart Contract Development', 'Smart Contract Development'), ('DApps Development', 'DApps Development'), ('NFT & Crypto Development', 'NFT & Crypto Development'), ('Cloud & DevOps', 'Cloud & DevOps'), ('Cloud Development', 'Cloud Development'), ('DevOps & CI/CD', 'DevOps & CI/CD'), ('Serverless Development', 'Serverless Development'), ('Cybersecurity & Ethical Hacking', 'Cybersecurity & Ethical Hacking'), ('Penetration Testing', 'Penetration Testing'), ('Secure Software Development', 'Secure Software Development'), ('Blockchain Security', 'Blockchain Security'), ('IoT Development', 'IoT Development'), ('Embedded IoT Solutions', 'Embedded IoT Solutions'), ('Edge Computing', 'Edge Computing'), ('Smart Home & Automation', 'Smart Home & Automation'), ('Database Development', 'Database Development'), ('SQL Database Development', 'SQL Database Development'), ('NoSQL Database Development', 'NoSQL Database Development'), ('Database Optimization & Management', 'Database Optimization & Management'), ('API & Integration Development', 'API & Integration Development'), ('RESTful API Development', 'RESTful API Development'), ('GraphQL Development', 'GraphQL Development'), ('Third-Party API Integration', 'Third-Party API Integration'), ('Robotics & Automation', 'Robotics & Automation'), ('Robotic Process Automation (RPA)', 'Robotic Process Automation (RPA)'), ('AI-Powered Automation', 'AI-Powered Automation')], help_text='Select a service from the list or leave it blank for others.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, help_text='Provide a description for the selected service or custom entry.'),
        ),
    ]

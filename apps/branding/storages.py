# branding/storages.py

from cloudinary_storage.storage import MediaCloudinaryStorage

class RawCloudinaryStorage(MediaCloudinaryStorage):
    def _get_upload_options(self, name):
        options = super()._get_upload_options(name)
        options['resource_type'] = 'raw'  # important for docs, pdfs, etc.
        return options

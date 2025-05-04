import os
from django.dispatch import receiver, Signal

def delete_profile_pic(sender, instance, **kwargs):
    """Delete the profile picture from filesystem."""
    if instance.image:
        print(instance.image.name)
        if instance.image.name != "default.png":
            path = instance.image.path
            os.remove(path)
            print("Profile picture deleted!")

# Define the signal without providing_args
profile_update_signal = Signal()

@receiver(profile_update_signal)
def profile_update_receiver(sender, **kwargs):
    """Signal receiver to handle profile image updates."""
    new_img = kwargs['new_img']
    old_img = kwargs['old_img']

    print(f"Old Image: {old_img.name}")
    print(f"New Image: {new_img.name}")

    # Check if the old image is different from the new image
    if old_img.name != new_img.name:
        path = old_img.path
        os.remove(path)  # Remove old image from the filesystem
        print("Deleted old profile image.")

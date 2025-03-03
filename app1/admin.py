from django.contrib import admin
from .models import Device
from django.utils.html import format_html

class DeviceAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('device_name', 'api_key', 'led1_status', 'led2_status', 'led3_status', 'led4_status', 'is_active', 'user', 'device_status')
    
    # Add filters for easier searching
    list_filter = ('is_active', 'user', 'led1_status', 'led2_status', 'led3_status', 'led4_status')
    
    # Enable search functionality
    search_fields = ('device_name', 'api_key', 'user__username')
    
    # Fields that can be clicked on in the list to go to the edit page
    list_display_links = ('device_name', 'api_key')
    
    # Make fields editable inline for quicker access (in the list view)
    list_editable = ('is_active', 'led1_status', 'led2_status', 'led3_status', 'led4_status')
    
    # Fields to be displayed on the detail view
    fields = ('device_name', 'api_key', 'user', 'is_active', 'led1_status', 'led2_status', 'led3_status', 'led4_status')
    
    # To use `format_html` for showing custom HTML in the admin (e.g., color-coded statuses)
    def device_status(self, obj):
        # Color-coding based on `is_active` status
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            'green' if obj.is_active else 'red',
            'Active' if obj.is_active else 'Inactive'
        )
    device_status.short_description = 'Device Status'

    # Add the `device_status` method as a readonly field
    readonly_fields = ('device_status',)

    # Custom save form or validation (optional)
    def save_model(self, request, obj, form, change):
        # Example of adding custom logic before saving (e.g., logging or altering data)
        if not obj.api_key:
            obj.api_key = 'Generated API Key'  # Placeholder for auto-generating API Key
        super().save_model(request, obj, form, change)

# Register the admin configuration for the Device model
admin.site.register(Device, DeviceAdmin)

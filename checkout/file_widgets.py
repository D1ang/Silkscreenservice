from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget to restyle the file input field.
    This is for the file input on the checkout form.
    """
    clear_checkbox_label = ('Remove')
    input_text = ('')
    template_name = (
        'checkout/custom_widget_templates/custom_clearable_file_input.html'
    )

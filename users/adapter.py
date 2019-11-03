from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.first_name = data.get('first_name')
        user.second_name = data.get('second_name')
        user.user_type = data.get('user_type')
        user.phone_number = data.get('phone_number')
        user.wants_to_receive_marketing_emails = data.get('wants_to_receive_marketing_emails')
        user.save()
        return user

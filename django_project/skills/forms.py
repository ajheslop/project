""" better comments """

from django import forms
from skills.models import SkillCategory, SkillSubCategory, SkillMain, UserSkill
from bootstrap_modal_forms.forms import BSModalModelForm


class SkillMainModelForm(BSModalModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = SkillMain
        fields = ['skill_name', 'skill_description']


class SkillCategoryModelForm(BSModalModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = SkillCategory
        fields = ['skill_category', 'skill_category_description']


class SkillSubCategoryModelForm(BSModalModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = SkillSubCategory
        fields = ['skill_sub_category', 'skill_sub_category_description']


class UserSkillModelForm(forms.models.ModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = UserSkill
        fields = ['user_skill', 'user_skill_category',
                  'user_skill_sub_category', ]


class UserSkillAuthorModelForm(forms.Form):
    """ better comments """
    names = UserSkill.objects.values_list(
        'author_id', 'author__username').distinct().order_by()

    team = forms.MultipleChoiceField(
        choices=names,
        widget=forms.SelectMultiple(),
        required=True,
        label='Team members',
    )


class UserSkillModelFormModal(BSModalModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = UserSkill
        fields = ['user_skill',
                  'user_skill_category',
                  'user_skill_sub_category',
                  'active',
                  'teach', ]


class UserSkillCreateModelForm(forms.models.ModelForm):
    """ better comments """

    class Meta:
        """ better comments """
        model = UserSkill
        fields = ['user_skill',
                  'user_skill_category',
                  'user_skill_sub_category',
                  'teach', ]

    def __init__(self, *args, **kwargs):
        """ better comments """
        for item in kwargs:
            print(item)
        user = kwargs.pop('user')
        super(UserSkillCreateModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            user_skill_query_set = UserSkill.objects.filter(
                author=user).values_list('user_skill__skill_name', flat=True)
            self.fields['user_skill'].queryset = SkillMain.objects.exclude(
                skill_name__in=user_skill_query_set)

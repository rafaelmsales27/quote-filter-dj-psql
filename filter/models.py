from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField

QUESTION_TYPES = (
    ('TEXT', 'Text'),
    ('EMAIL', 'Email'),
    ('PHONE', 'Phone Number'),
    ('NUMBER', 'Number'),
    ('DATE', 'Date'),
    ('BOOLEAN', 'True/False'),
    ('CHOICE', 'Choice'),
)


class Question(models.Model):
    question_text = models.TextField(null=False)  # Mandatory question text
    order = models.SmallIntegerField(null=False)  # Order for sorting questions
    type = models.CharField(max_length=20, choices=QUESTION_TYPES, null=False)  # Predefined question types
    options = ArrayField(models.CharField(max_length=50), blank=True)  # Optional options
    active = models.BooleanField(null=False, default=True)  # Flag for active/inactive questions
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question_text[:20]}..."


class Quote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Enforce data integrity
    answer = models.CharField(max_length=255, blank=True)  # Default for text answers
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer for question: {self.question.question_text[:20]}..."

    # Custom validation for specific question types
    def clean(self):
        cleaned_data = super().clean()  # Get cleaned data from parent
        question_type = self.question.type

        if question_type == 'TEXT':
            # No specific validation needed for text answers
            pass
        elif question_type == 'EMAIL':
            # Validate email format
            import re
            email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,}$"
            if not re.match(email_regex, self.answer):
                raise forms.ValidationError('Invalid email format')
        elif question_type == 'PHONE':
            # Validate phone number format (custom regex)
            phone_regex = r"^[\+\d\-\(\)]+$"  # Example for basic phone number format
            if not re.match(phone_regex, self.answer):
                raise forms.ValidationError('Invalid phone number format')
        elif question_type == 'DATE':
            # Validate date format (custom regex)
            date_regex = r"^\d{2}-\d{2}-\d{4}$"  # Example for DD-MM-YYYY format
            if not re.match(date_regex, self.answer):
                raise forms.ValidationError('Invalid date format (DD-MM-YYYY expected)')
        else:
            raise forms.ValidationError('Invalid question type')

        return cleaned_data

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_login_view(client, django_user_model):
    # Create a test user
    user = django_user_model.objects.create_user(
        username="test@example.com",  # Explicitly set username
        email="test@example.com",
        password="securepass",
    )

    # Attempt login
    response = client.post(
        reverse("accounts:login"),
        {
            "username": "test@example.com",  # Django's default login form uses "username" field
            "password": "securepass",
        },
    )

    assert response.status_code == 302  # Redirects on successful login
    assert response.url == reverse("taskmanager:task-list")


@pytest.mark.django_db
def test_register_view(client):
    data = {
        "email": "newuser@example.com",
        "password": "strongpassword123",  # This is the field name for the password
        "confirm_password": "strongpassword123",  # Add the confirm_password field
        "first_name": "John",
        "last_name": "Doe",
    }

    response = client.post(reverse("accounts:register"), data)

    # Check if we got a redirect after successful form submission
    assert (
        response.status_code == 302
    ), f"Expected 302 but got {response.status_code}. Errors: {response.context['form'].errors if 'form' in response.context else 'No form errors'}"
    assert response.url == reverse("accounts:login")

    # Check if user was created in the database
    assert User.objects.filter(email="newuser@example.com").exists()

    # Verify the password is correctly hashed
    user = User.objects.get(email="newuser@example.com")
    assert user.check_password("strongpassword123")


@pytest.mark.django_db
@pytest.mark.parametrize(
    "view_name, template",
    [
        ("accounts:about", "pages/about.html"),
        ("accounts:contact", "pages/contact.html"),
    ],
)
def test_template_views(client, view_name, template):
    response = client.get(reverse(view_name))
    assert response.status_code == 200
    assert template in [t.name for t in response.templates]

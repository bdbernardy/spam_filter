from app.core.models.config_base import to_camel


def test_to_camel_should_convert_python_name_to_camel():
    # Arrange
    input = "python_name"
    except_output = "pythonName"

    # Act
    output = to_camel(input)

    # Assert
    assert output == except_output

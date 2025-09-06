import pytest
import unittest.mock as mock
import service as service

# mock testing from custom db
@mock.patch("service.get_user_name_from_db")
def test_get_user_name_from_db(mock_get_user_name_from_db):
    mock_get_user_name_from_db.return_value = "Ben"
    assert service.get_user_name_from_db(1) == "Ben"
    
    
# mock testing from api
@mock.patch("service.requests.get")
def test_get_user_data(mock_user_data):
    
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "Ben Tennyson",
        "email": "ben10@hero.com"
    }
    mock_user_data.return_value = mock_response
    
    result = service.get_user_data(1)    # Calling the function under test
    
    # assertions
    assert result['name'] == "Ben Tennyson"
    assert result['email'] == "ben10@hero.com"
    
    # Verify API was called correctly
    mock_user_data.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")


# mock testing from failure api 
@mock.patch("service.requests.get")
def test_get_user_data_failure(mock_user_data):
    
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_user_data.return_value =  mock_response
    
    result = service.get_user_data(100)
    assert result == {"error": "User not found"}
    mock_user_data.assert_called_once_with("https://jsonplaceholder.typicode.com/users/100")

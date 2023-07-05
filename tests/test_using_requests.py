def test_get_user(session, adapter):
    mock_response = {
        'id': 1,
        'name': 'John Wick',
        'username': 'JW',
        'email': 'housekeeping@wick.ok',
        'address': {
            'street': 'Kulas Light',
            'suite': 'Apt. 556',
            'city': 'Gwenborough',
            'zipcode': '92998-3874',
            'geo': {'lat': '-37.3159', 'lng': '81.1496'}
        },
        'phone': '1-770-736-8031 x56442',
        'website': 'hildegard.org',
    }

    # Start mocking requests
    adapter.register_uri('GET', 'mock://test.com/users/1', json=mock_response)
    resp = session.get("mock://test.com/users/1")
    assert resp.json() == mock_response

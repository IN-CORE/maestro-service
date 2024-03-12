import requests

API_V2_STR = "http://localhost:8000"
dataset_id = "65ef6a9bdc75ad0c3653ebe0"


def test_post_retrofit_strategy_details():
    rsdetails = {
        "total": {
            "num_bldg": 3283,
            "num_bldg_no_cost": 42,
            "cost": 117260721.43
        },
        "by_rule": {
            "0": {
                "num_bldg": 3191,
                "num_bldg_no_cost": 40,
                "cost": 94393478.73
            },
            "1": {
                "num_bldg": 90,
                "num_bldg_no_cost": 0,
                "cost": 22867242.7
            },
            "2": {
                "num_bldg": 2,
                "num_bldg_no_cost": 2,
                "cost": 0
            }
        }
    }

    response = requests.post(f"{API_V2_STR}/maestro/datasets/{dataset_id}/rsdetails", json=rsdetails)
    assert response.status_code == 200  # or another status code you expect

    response_data = response.json()
    assert 'dataset_id' in response_data  # check if dataset_id is in the response
    assert response_data['dataset_id'] == dataset_id  # verify the dataset_id matches

    # duplicate entry doesn't allowed
    response = requests.post(f"{API_V2_STR}/maestro/datasets/{dataset_id}/rsdetails", json=rsdetails)
    assert response.status_code == 400  # or another status code you expect


def test_get_retrofit_strategy_details():
    response = requests.get(f"{API_V2_STR}/maestro/datasets/{dataset_id}/rsdetails")
    assert response.status_code == 200

    response_data = response.json()
    assert 'dataset_id' in response_data
    assert response_data['dataset_id'] == dataset_id
    assert 'total' in response_data
    assert 'by_rule' in response_data
    assert response_data['total']['num_bldg'] == 3283
    assert response_data['by_rule']['1']['num_bldg'] == 90


def test_delete_retrofit_strategy_details():
    response = requests.delete(f"{API_V2_STR}/maestro/datasets/{dataset_id}/rsdetails")
    assert response.status_code == 200

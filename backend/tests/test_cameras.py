def test_camera_pagination(client):
  response = client.get("/cameras?page=1&limit=5")
  data = response.json()

  assert response.status_code == 200
  assert "data" in data
  assert "total" in data
  assert len(data["data"]) <= 5

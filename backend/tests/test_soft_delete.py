def test_soft_delete_camera(client):
  response = client.delete("/cameras/CAM-001")
  assert response.status_code == 200
  res = client.get("/cameras")
  data = res.json()
  ids = [c["id"] for c in data["data"]]
  assert "CAM-001" not in ids

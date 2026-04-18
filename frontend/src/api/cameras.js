import api from "./axios";

export const getCameras = (params) =>
  api.get("/cameras/", { params });

export const createCamera = (data) =>
  api.post("/cameras/", data);

export const updateCamera = (id, data) =>
  api.put(`/cameras/${id}`, data);

export const deleteCamera = (id) =>
  api.delete(`/cameras/${id}`);

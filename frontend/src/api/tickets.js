import api from "./axios";

export const getTickets = (params) =>
  api.get("/tickets/", { params });

export const createTicket = (data) =>
  api.post("/tickets/", data);

export const updateTicketStatus = (id, status) =>
  api.patch(`/tickets/${id}/status`, {
    new_status: status,
  });

export const deleteTicket = (id) =>
  api.delete(`/tickets/${id}`);

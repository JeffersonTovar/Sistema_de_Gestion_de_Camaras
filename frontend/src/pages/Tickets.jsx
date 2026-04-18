import { useEffect, useState } from "react";
import {
  getTickets,
  updateTicketStatus,
} from "../api/tickets";

import TicketTable from "../components/tickets/TicketTable";

export default function Tickets() {
  const [tickets, setTickets] = useState([]);
  const fetchData = async () => {
    const res = await getTickets();
    setTickets(res.data.data);
  };
  useEffect(() => {
    fetchData();
  }, []);
  const handleStatusChange = async (id, status) => {
    await updateTicketStatus(id, status);
    fetchData();
  };
  return (
    <div style={{ padding: 20 }}>
      <h2>Tickets de Mantenimiento</h2>
      <TicketTable
        data={tickets}
        onChangeStatus={handleStatusChange}
      />
    </div>
  );
}

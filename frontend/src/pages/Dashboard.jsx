import { useEffect, useState } from "react";
import { getDashboardData } from "../api/dashboard";
import { getCameras } from "../api/cameras";

import KPICards from "../components/dashboard/KPICards";
import CameraStatusChart from "../components/dashboard/CameraStatusChart";
import TicketsPriorityChart from "../components/dashboard/TicketsPriorityChart";
import CameraMap from "../components/map/CameraMap";

import { Grid, Typography, Box, Divider } from "@mui/material";

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [cameras, setCameras] = useState([]);

  useEffect(() => {
    const load = async () => {
      try {
        const [dashRes, camsRes] = await Promise.all([
          getDashboardData(),
          getCameras({ limit: 100 })
        ]);

        setData(dashRes.data);
        setCameras(camsRes.data.data);
      } catch (error) {
        console.error("Error cargando dashboard:", error);
      }
    };

    load();
  }, []);

  if (!data) return <p>Cargando...</p>;

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Dashboard de Videovigilancia
      </Typography>

      <KPICards data={data.kpis} />

      <Grid container spacing={4} sx={{ mt: 2 }}>
        <Grid item xs={12} md={6}>
          <Typography variant="h6" gutterBottom>
            Estado de Cámaras
          </Typography>
          <CameraStatusChart data={data.cameraStatus} />
        </Grid>

        <Grid item xs={12} md={6}>
          <Typography variant="h6" gutterBottom>
            Tickets por Prioridad
          </Typography>
          <TicketsPriorityChart data={data.ticketsPriority} />
        </Grid>
      </Grid>

      <Divider sx={{ my: 4 }} />

      <Box>
        <Typography variant="h6" gutterBottom>
          Mapa de Cámaras en Bogotá
        </Typography>
        <CameraMap cameras={cameras} />
        <Box sx={{ mt: 2 }}>
          <span style={{ color: "green" }}>● Activa</span>{" | "}
          <span style={{ color: "orange" }}>● En Mantenimiento</span>{" | "}
          <span style={{ color: "red" }}>● Inactiva</span>
        </Box>
      </Box>
    </Box>
  );
}

import { Grid, Card, CardContent, Typography } from "@mui/material";

export default function KPICards({ data }) {
  const kpis = [
    { label: "Cámaras Activas", value: data.activeCameras },
    { label: "Tickets Abiertos", value: data.openTickets },
    { label: "Tickets Críticos", value: data.criticalTickets },
    { label: "Prom. Resolución (días)", value: data.avgResolutionTime },
  ];

  return (
    <Grid container spacing={2}>
      {kpis.map((kpi) => (
        <Grid item xs={12} sm={6} md={3} key={kpi.label}>
          <Card>
            <CardContent>
              <Typography variant="subtitle2">
                {kpi.label}
              </Typography>
              <Typography variant="h5">
                {kpi.value}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
}

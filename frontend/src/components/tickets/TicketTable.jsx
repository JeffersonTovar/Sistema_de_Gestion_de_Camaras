import { DataGrid } from "@mui/x-data-grid";
import { Button, Chip } from "@mui/material";

const STATUS_COLOR = {
  "Nuevo": "default",
  "En curso": "warning",
  "Resuelto": "success",
};

export default function TicketTable({ data, onChangeStatus }) {
  const columns = [
    { field: "id", headerName: "ID", width: 140 },

    {
      field: "camera_id",
      headerName: "Cámara",
      width: 120,
    },

    {
      field: "type",
      headerName: "Tipo",
      width: 140,
    },

    {
      field: "priority",
      headerName: "Prioridad",
      width: 120,
    },

    {
      field: "status",
      headerName: "Estado",
      width: 150,
      renderCell: (params) => (
        <Chip
          label={params.value}
          color={STATUS_COLOR[params.value]}
        />
      ),
    },

    {
      field: "actions",
      headerName: "Acciones",
      width: 300,
      renderCell: (params) => {
        const status = params.row.status;

        return (
          <>
            {status === "Nuevo" && (
              <Button
                size="small"
                onClick={() =>
                  onChangeStatus(params.row.id, "En curso")
                }
              >
                Iniciar
              </Button>
            )}

            {status === "En curso" && (
              <Button
                size="small"
                color="success"
                onClick={() =>
                  onChangeStatus(params.row.id, "Resuelto")
                }
              >
                Resolver
              </Button>
            )}

            {status === "Resuelto" && (
              <Button size="small" disabled>
                Finalizado
              </Button>
            )}
          </>
        );
      },
    },
  ];

  return (
    <div style={{ height: 600, width: "100%" }}>
      <DataGrid
        rows={data}
        columns={columns}
        getRowId={(row) => row.id}
        pageSizeOptions={[5, 10, 20]}
      />
    </div>
  );
}

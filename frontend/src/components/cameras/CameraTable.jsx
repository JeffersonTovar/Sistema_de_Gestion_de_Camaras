import { DataGrid } from "@mui/x-data-grid";
import { Button } from "@mui/material";

export default function CameraTable({ data, onEdit, onDelete }) {
  const columns = [
    { field: "id", headerName: "ID", width: 120 },
    { field: "model", headerName: "Modelo", flex: 1 },
    { field: "location", headerName: "Ubicación", flex: 1 },
    { field: "status", headerName: "Estado", width: 150 },
    { field: "locality", headerName: "Localidad", width: 150 },

    {
      field: "actions",
      headerName: "Acciones",
      width: 200,
      renderCell: (params) => (
        <>
          <Button
            size="small"
            onClick={() => onEdit(params.row)}
          >
            Editar
          </Button>

          <Button
            size="small"
            color="error"
            onClick={() => onDelete(params.row.id)}
          >
            Eliminar
          </Button>
        </>
      ),
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

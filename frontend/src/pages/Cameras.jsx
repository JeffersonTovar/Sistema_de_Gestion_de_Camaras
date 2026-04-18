import { useEffect, useState } from "react";
import {
  getCameras,
  createCamera,
  updateCamera,
  deleteCamera,
} from "../api/cameras";

import CameraTable from "../components/cameras/CameraTable";
import CameraForm from "../components/cameras/CameraForm";

import { Dialog, Button } from "@mui/material";

export default function Cameras() {
  const [cameras, setCameras] = useState([]);
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState(null);

  const fetchData = async () => {
    const res = await getCameras();
    setCameras(res.data.data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSave = async (data) => {
    try {
      if (selected) {
        await updateCamera(selected.id, data);
      } else {
        await createCamera(data);
      }
      setOpen(false);
      setSelected(null);
      fetchData();
    } catch (err) {
      alert(err.response?.data?.detail || "Error al guardar cámara");
    }
  };

  const handleDelete = async (id) => {
    await deleteCamera(id);
    fetchData();
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Cámaras</h2>

      <Button variant="contained" onClick={() => setOpen(true)}>
        Nueva Cámara
      </Button>

      <CameraTable
        data={cameras}
        onEdit={(cam) => {
          setSelected(cam);
          setOpen(true);
        }}
        onDelete={handleDelete}
      />

      <Dialog open={open} onClose={() => setOpen(false)} fullWidth>
        <div style={{ padding: 20 }}>
          <CameraForm
            initialData={selected}
            onSubmit={handleSave}
            onClose={() => setOpen(false)}
          />
        </div>
      </Dialog>
    </div>
  );
}

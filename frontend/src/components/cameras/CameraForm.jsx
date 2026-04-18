import { useState, useEffect } from "react";
import { TextField, Button, MenuItem, Box } from "@mui/material";

const STATUS = ["Activa", "Inactiva", "En Mantenimiento"];

export default function CameraForm({ initialData, onSubmit, onClose }) {
  const [form, setForm] = useState({
    id: "",
    model: "",
    location: "",
    lat: "",
    lng: "",
    status: "Activa",
    locality: "",
  });

  useEffect(() => {
    if (initialData) setForm(initialData);
  }, [initialData]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    if (!form.id || form.id.trim() === "") {
      alert("ID es obligatorio");
      return;
    }

    onSubmit({
      ...form,
      lat: parseFloat(form.lat),
      lng: parseFloat(form.lng),
    });
  };

  return (
    <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
      <TextField
        label="ID"
        name="id"
        value={form.id}
        onChange={handleChange}
        disabled={!!initialData}
      />

      <TextField
        label="Modelo"
        name="model"
        value={form.model}
        onChange={handleChange}
      />

      <TextField
        label="Ubicación"
        name="location"
        value={form.location}
        onChange={handleChange}
      />

      <TextField
        type="number"
        label="Latitud"
        name="lat"
        value={form.lat}
        onChange={handleChange}
      />

      <TextField
        type="number"
        label="Longitud"
        name="lng"
        value={form.lng}
        onChange={handleChange}
      />

      <TextField
        select
        label="Estado"
        name="status"
        value={form.status}
        onChange={handleChange}
      >
        {STATUS.map((s) => (
          <MenuItem key={s} value={s}>
            {s}
          </MenuItem>
        ))}
      </TextField>

      <TextField
        label="Localidad"
        name="locality"
        value={form.locality}
        onChange={handleChange}
      />

      <Button variant="contained" onClick={handleSubmit}>
        Guardar
      </Button>
    </Box>
  );
}

import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";


import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

const DefaultIcon = L.icon({
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

L.Marker.prototype.options.icon = DefaultIcon;


const getColor = (status) => {
  switch (status) {
    case "Activa":
      return "green";
    case "En Mantenimiento":
      return "orange";
    case "Inactiva":
      return "red";
    default:
      return "blue";
  }
};


const createIcon = (color) =>
  L.divIcon({
    className: "custom-marker",
    html: `<div style="
      background:${color};
      width:14px;
      height:14px;
      border-radius:50%;
      border:2px solid white;
    "></div>`,
  });

export default function CameraMap({ cameras }) {
  return (
    <MapContainer
      center={[4.65, -74.1]}
      zoom={12}
      style={{ height: "500px", width: "100%" }}
    >
      <TileLayer
        attribution="&copy; OpenStreetMap"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {cameras.map((cam) => (
        <Marker
          key={cam.id}
          position={[cam.lat, cam.lng]}
          icon={createIcon(getColor(cam.status))}
        >
          <Popup>
            <b>{cam.id}</b> <br />
            {cam.model} <br />
            {cam.location} <br />
            Estado: {cam.status} <br />
            Últ. Mantto: {cam.last_maintenance_date}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

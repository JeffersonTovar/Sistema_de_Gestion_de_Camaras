import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
} from "recharts";

const COLORS = {
  Activa: "#4caf50",
  "En Mantenimiento": "#ff9800",
  Inactiva: "#f44336",
};

export default function CameraStatusChart({ data }) {
  return (
    <PieChart width={400} height={300}>
      <Pie
        data={data}
        dataKey="value"
        nameKey="name"
        outerRadius={120}
        label
      >
        {data.map((entry) => (
          <Cell
            key={entry.name}
            fill={COLORS[entry.name]}
          />
        ))}
      </Pie>

      <Tooltip />
      <Legend />
    </PieChart>
  );
}

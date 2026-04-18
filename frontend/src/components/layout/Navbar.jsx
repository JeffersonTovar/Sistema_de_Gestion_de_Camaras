import { AppBar, Toolbar, Button } from "@mui/material";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Button color="inherit" component={Link} to="/">
          Dashboard
        </Button>
        <Button color="inherit" component={Link} to="/cameras">
          Cámaras
        </Button>
        <Button color="inherit" component={Link} to="/tickets">
          Tickets
        </Button>
      </Toolbar>
    </AppBar>
  );
}

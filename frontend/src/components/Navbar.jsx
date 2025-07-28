import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

const Logo = styled("img")({
  height: 36,
  marginRight: 8,
});

export default function NavBar({ onAddClick }) {
  return (
    <AppBar
      position="fixed"
      elevation={1}
      sx={{
        backgroundColor: "#f5f5f5", 
        color: "#0A1929",           
        px: 2,
        width: "100%",
      }}
    >
      <Toolbar sx={{ justifyContent: "space-between" }}>
        {/* logo and title in the top left */}
        <Box display="flex" alignItems="center">
          <Logo src="/LeetTrack_Logo.png" alt="LeetTrack Logo" />
          <Typography
            variant="h6"
            sx={{ fontWeight: 700, color: "#0A1929" }}
          >
            LeetTrack
          </Typography>
        </Box>

        {/* add problem button in the top right */}
        <Button
          onClick={onAddClick}
          variant="contained"
          sx={{
            backgroundColor: "#0A1929",
            color: "#ffffff",
            textTransform: "none",
            fontWeight: 600,
            "&:hover": {
              backgroundColor: "#07121f",
            },
          }}
        >
          Add Problem
        </Button>
      </Toolbar>
    </AppBar>
  );
}

import NavBar from "../components/Navbar";

function Dashboard() {
  const handleAddClick = () => {
    // placeholder for future modal
  };

  return (
    <div>
      <NavBar onAddClick={handleAddClick} />
      {/* dashboard content goes here */}
    </div>
  );
}

export default Dashboard;
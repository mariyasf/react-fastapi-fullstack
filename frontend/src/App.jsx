import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import heroImg from "./assets/hero.png";
import axios from "axios";

function App() {
  const featchData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/");
      console.log(res.data);
    } catch (error) {
      console.log("error", console.error(error));
    }
  };
  useEffect(() => {
    featchData();
  }, []);
  return (
    <>
      <main>Wellcome </main>
    </>
  );
}

export default App;

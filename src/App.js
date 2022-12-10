import { BrowserRouter, Routes, Route } from "react-router-dom";
import DefaultLayout from "./layouts/default_layout";
import Error404 from "./pages/404";
import Login from "./pages/login";
import Register from "./pages/register";
import Account from "./pages/account";
import Home from "./pages/home";
import Product from "./pages/products";
// import Jobs from "../pages/jobs";
// import Hire from "../pages/hire";
// import About from "../pages/about";
// import Blog from "../pages/hblog";
//import "./App.css";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<DefaultLayout />}>
            <Route index element={<Home />} />
            <Route path="404" element={<Error404 />} />
            <Route path="products" element={<Product />} />
            <Route path="account" element={<Account />} />
            {/* <Route path="jobs" element={<Jobs />} />
            <Route path="hire" element={<Hire />} />
            <Route path="about" element={<About />} />
            <Route path="blog" element={<Blog />} /> */}
          </Route>
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;

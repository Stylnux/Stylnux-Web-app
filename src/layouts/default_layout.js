import { Outlet } from "react-router-dom";
import Header from "../components/header";

export const DefaultLayout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
};
export default DefaultLayout;

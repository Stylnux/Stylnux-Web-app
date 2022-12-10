import { Link, NavLink } from "react-router-dom";
import { Image } from "@chakra-ui/react";
import { Input, InputLeftElement, InputRightElement, InputGroup, Icon, Avatar, Link as ReachLink } from "@chakra-ui/react";
import { Menu, MenuButton, MenuList, MenuItem } from "@chakra-ui/react";
import { CiSearch } from "react-icons/ci";
import { RiArrowDownSLine, RiArrowUpSLine } from "react-icons/ri";
import { DefaultMenu, Profile } from "../json/nav";

import "../styles/header.scss";

export const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light" style={{ backgroundColor: "#EFF6FF" }}>
      <div className="container-fluid mx-5">
        <Link as={ReachLink} className="navbar-brand" to="/">
          <Image src="./assets/img/logo.png" width="150px" height="50px" alt="logo" />
        </Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown-2" aria-controls="navbarNavDropdown-2" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse " id="navbarNavDropdown-2">
          <InputGroup width="40%" mx="auto">
            <InputLeftElement pointerEvents="none" children={<Icon as={CiSearch} color="gray.300" />} />
            <Input type="tel" placeholder="Search" />
            <InputRightElement
              children={
                <Menu placement="bottom-end" offset="[99,0]">
                  <MenuButton color="gray.300">
                    <RiArrowDownSLine />
                  </MenuButton>
                  <MenuList>
                    <MenuItem>Download</MenuItem>
                    <MenuItem>Create a Copy</MenuItem>
                    <MenuItem>Mark as Draft</MenuItem>
                    <MenuItem>Delete</MenuItem>
                    <MenuItem>Attend a Workshop</MenuItem>
                  </MenuList>
                </Menu>
              }
            />
          </InputGroup>
          <ul className="ml-auto navbar-nav justify-content-evenly" style={{ width: "50%" }}>
            {DefaultMenu.map((nav, index) => {
              return (
                <li className="nav-item" key={index}>
                  <NavLink as={ReachLink} to={nav.path} className={({ isActive }) => (isActive ? "active-nav nav-NavLink" : "nav-NavLink")}>
                    {nav.name}
                  </NavLink>
                </li>
              );
            })}
          </ul>
          <Link as={ReachLink} to={Profile.account.path}>
            <Avatar size="sm" name="Dan Abrahmov" src="https://bit.ly/dan-abramov" />
          </Link>
        </div>
      </div>
    </nav>
  );
};
export default Header;

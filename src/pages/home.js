import { Link } from "react-router-dom";
import { Link as ReachLink } from "@chakra-ui/react";

export const Home = () => {
  return (
    <div className="container mx-auto">
      <h3 className="ms-5 mb-2 text-success fw-bolder mt-5"> Completed Links</h3>
      <ul className="ms-5">
        <li>
          <Link as={ReachLink} to="login" className="fw-bold text-muted">
            &nbsp;Sign In
          </Link>
        </li>
        <li>
          <Link as={ReachLink} to="register" className="fw-bold text-muted">
            &nbsp;Register
          </Link>
        </li>
        <li>
          <Link as={ReachLink} to="404" className="fw-bold text-muted">
            &nbsp;404
          </Link>
        </li>
        <li>
          <Link as={ReachLink} to="account" className="fw-bold text-muted">
            &nbsp;Account
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Home;

import { Link } from "react-router-dom";
import { Image, Link as ReachLink } from "@chakra-ui/react";
export const Error404 = () => {
  return (
    <section className="bg-light pb-5 pt-5 text-center">
      <div className="container pb-5 pt-5">
        <div className="row">
          <div className="col-lg-8 mx-auto">
            <Image src="./assets/img/404.png" width="600px" className="mx-auto" alt="404" />
            <p className="fw-bolder mb-4 text-secondary">Browse more jobs while we fix this</p>
            <Link as={ReachLink} to="/" className="btn btn-warning text-white">
              BACK TO HOME
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};
export default Error404;

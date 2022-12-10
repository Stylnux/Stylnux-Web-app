import { useState } from "react";
import { Link } from "react-router-dom";
import { Avatar, Link as ReachLink } from "@chakra-ui/react";
import { Rating } from "@smastrom/react-rating";
import "@smastrom/react-rating/style.css";

export const Account = () => {
  const [rating, setRating] = useState(0);
  return (
    <section className="bg-light pb-5 pt-5">
      <div className="container pb-4 pt-4">
        <header>
          <h1 className="bg-warning h5 pb-2 ps-4 pt-2 rounded text-white w-50">Your Account</h1>
        </header>
        <div className="align-items-center row">
          <div className="col-md-3">
            <div className="gy-0 row">
              <div className="col-12 ">
                <div className="card mb-3 ">
                  <Avatar size="lg" name="Dan Abrahmov" mx="auto" mt="5" src="https://bit.ly/dan-abramov" />
                  <div className="card-body">
                    <h5 className="card-title fw-bold h5 mb-0 text-center text-dark">Omar A. George</h5>
                    <p className="card-text mb-0 text-center text-secondary">
                      <small>omarageorge@gmail.com</small>
                    </p>
                    <p className="card-text text-center text-secondary">
                      <small>Lagos, Nigeria</small>
                    </p>
                    <button className="btn btn-sm btn-warning d-block fw-normal h6 mx-auto mt-3 text-center text-white" type="button">
                      EDIT PROFILE
                    </button>
                    <p className="card-text text-secondary row">
                      <small className="fw-bolder text-body col-5 text-end">Ratings</small>
                      <Rating style={{ maxWidth: "40%" }} className="col-6 text-start ps-0" value={rating} onChange={setRating} halfFillMode="svg" />
                    </p>
                  </div>
                </div>
              </div>
              <div className="col-12 ">
                <div className="card mb-3 ">
                  <div className="card-body">
                    <p className="card-text mb-2 text-left">
                      <Link as={ReachLink} to="">
                        <small className="fw-bold text-muted">Order</small>
                      </Link>
                    </p>
                    <p className="card-text mb-2 text-left">
                      <Link as={ReachLink} to="">
                        <small className="fw-bold text-muted">Shipping Address</small>
                      </Link>
                    </p>
                    <p className="card-text mb-2 text-left">
                      <Link as={ReachLink} to="">
                        <small className="fw-bold text-muted">Payments &amp; Credits</small>
                      </Link>
                    </p>
                    <p className="card-text mb-2 text-left">
                      <Link as={ReachLink} to="">
                        <small className="fw-bold text-muted">Returns</small>
                      </Link>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="align-self-baseline col-md-7">
            <div className="card mb-3">
              <div className="card-body mb-5 mt-5">
                <h5 className="card-title fw-bolder h5 mt-5 text-center text-muted">No orders yet</h5>
                <p className="card-text text-center text-muted">
                  <small>Looks like you haven't placed any order yet</small>
                </p>
                <button className="btn btn-sm btn-warning d-block fw-normal h6 mb-5 mt-3 mx-auto px-4 text-center text-white" type="button">
                  CONTINUE TO DASHBOARD
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
export default Account;

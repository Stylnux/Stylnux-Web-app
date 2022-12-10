import { Link } from "react-router-dom";
import { Link as ReachLink } from "@chakra-ui/react";
export const Register = () => {
  return (
    <section className="pb-5 pt-5" style={{ backgroundColor: "#AAAAAA" }}>
      <div className="container pb-5 pt-5">
        <div className="col-md-9 col-xl-8 mx-auto">
          <div className="bg-white pb-2 px-4 pt-2">
            <h2 className="fw-bold h4 mb-1 mx-auto text-center text-dark">WELCOME</h2>
            <p className="fw-bold mb-0 mt-3 text-dark">Create your account to join</p>
            <p className="h6 mb-4 text-secondary">Create an account and discover the best marketplace</p>
            <p className="mb-4" />
            <form>
              <div className="row gy-3 justify-content-between">
                <div className="col-md-5">
                  <label htmlFor="name" className="h6 text-secondary form-label">
                    Name
                  </label>
                  <input type="text" className="form-control text-secondary" placeholder="Your name" id="name" style={{ backgroundColor: "#EFF6FF" }} />
                </div>
                <div className="col-md-5">
                  <label htmlFor="phone" className="h6 text-secondary form-label">
                    Phone number
                  </label>
                  <input type="phone" className="form-control text-secondary" placeholder="Your name" id="phone" style={{ backgroundColor: "#EFF6FF" }} />
                </div>
                <div className="col-md-5">
                  <label htmlFor="email" className="h6 text-secondary form-label">
                    Email
                  </label>
                  <input type="email" className="form-control text-secondary" placeholder="Your email" id="email" style={{ backgroundColor: "#EFF6FF" }} />
                </div>
                <div className="col-md-5">
                  <label htmlFor="password" className="h6 text-secondary form-label">
                    Password
                  </label>
                  <input type="password" className="form-control text-secondary" placeholder="Your password" id="password" style={{ backgroundColor: "#EFF6FF" }} defaultValue={123456} />
                </div>
              </div>
              <button type="submit" className="btn btn-sm btn-warning d-block fw-bold mb-3 mx-auto mt-3 pb-2 px-5 pt-2 text-white">
                Register
              </button>
              <p className="mb-0 text-center text-secondary">
                <small>
                  Have an account?&nbsp;
                  <Link as={ReachLink} to="" className="fw-bold text-muted">
                    &nbsp;Sign In
                  </Link>
                </small>
              </p>
              <p className="mb-4 text-center text-secondary">
                <small>
                  By Clicking Register you agree to our&nbsp;&nbsp;
                  <Link as={ReachLink} to="" className="fw-bold text-muted">
                    Terms and Data Policy&nbsp;
                  </Link>
                </small>
              </p>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};
export default Register;

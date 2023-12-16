import Logo from '../assets/logo1.jpg';

const Navbar = () => {
  // Add any necessary logic here

  return (
    <div>
      <header className="navbar-container d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
      <div className="col-md-3 mb-2 mb-md-0">
        <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
            <img className='logo' src={Logo} alt="Your Image" width="50" height="50" />
            <h2 className='appName'>Sanjaya</h2>
          </a>
      </div>

      <div className="col-md-3 text-end">
      <button type="button" className="btn btn-outline-primary me-2">Login</button>
        <button type="button" className="btn btn-primary">sign in</button>
      </div>
    </header>
    </div>
  );
};

export default Navbar;
import {useState, useEffect} from "react";
import axios from "axios";
import {BrowserRouter as Router, Route, Routes, useLocation, useNavigate} from "react-router-dom";
import Login from "./components/Login.jsx";
import Navbar from "./components/Navbar.jsx";
import AboutUs from "./pages/AboutUs.jsx";
import NotFound from "./pages/404.jsx";
import {AnimatePresence} from "framer-motion";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import CustomUserForm from "./components/NewUser.jsx";


const AnimateRoutes = () => {
    const location = useLocation();
    return (
        <AnimatePresence mode="wait">
            <Routes location={location} key={location.key}>
                <Route path="/login" element={<Login />} />
                <Route path="/about" element={<AboutUs />} />
                <Route path="/userform" element={<CustomUserForm />} />
                <Route path="/userform/:id" element={<CustomUserForm isEditMode={true} />} />
                <Route path="/" element={<Home />} />
                <Route path="*" element={<NotFound />} /> {/* 404 personalizado */}
            </Routes>
        </AnimatePresence>
    )
}

// Home component

function Home() {
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const session = localStorage.getItem('accessToken');
    const navigate = useNavigate();


     useEffect(() => {
        axios.get('http://127.0.0.1:8000/users/api/')
            .then((response) => {
                setData(response.data)
                setLoading(false)
            })
            .catch((error) => {
                setError('Error al obtener los datos ' + error)
                setLoading(false)
            })
    },[])

    const handleDelete = (id) => {
    if (window.confirm("Are you sure you want to delete this user?")) {
        axios.delete(`http://127.0.0.1:8000/users/form/${id}/`)
            .then((response) => {
                alert(response.data.message);
                setData(data.filter(user => user.id !== id));
            })
            .catch((error) => {
                alert("There was an error deleting the user.");
                console.error("Error deleting the user", error);
            });
    }
};

     const handleUpdate = (id) => {
        navigate(`/userform/${id}`, { state: { isEditMode: true, currentUser: data.find(user => user.id === id) } });
    };

    if(loading){
        return <div>Cargando...</div>
    }
    if(error){
        return <div>Error: {error}</div>
    }
    return (
        <div>
            <h1>Datos de la API desde Django</h1>
            <br/>
            <p>{session}</p>

              <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Email</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((user) => (
                        <tr key={user.id}>
                            <td>{user.name}</td>
                            <td>{user.surname}</td>
                            <td>{user.email}</td>
                            <td>
                                <button className="btn btn-primary me-2" onClick={() => handleUpdate(user.id)}>Update</button>
                                <button className="btn btn-danger" onClick={() => handleDelete(user.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

function App() {
    return (
        <Router>
            <Navbar />
            <div className="container mt-4">
                <div className="col">
                    <AnimateRoutes />
                </div>
            </div>
        </Router>
    )
}

export default App


import {useState, useEffect} from "react";
import axios from "axios";
import {BrowserRouter as Router, Route, Routes, useLocation} from "react-router-dom";
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

    if(loading){
        return <div>Cargando...</div>
    }
    if(error){
        return <div>Error: {error}</div>
    }
    return (
        <div>
            <h1>Datos de la API desde Django</h1>
            <h2>{session}</h2>
            <ul>
                {data.map((item)=> (
                    <li key={item.id}>{JSON.stringify(item)}</li>
                ))}
            </ul>
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


import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useLocation } from "react-router-dom";

const CustomUserForm = ({ isEditMode = false }) => {
    const [formFields, setFormFields] = useState([]);
    const [formData, setFormData] = useState({
        email: "",
        name: "",
        surname: "",
        control_number: "",
        age: "",
        tel: "",
        password1: "",
        password2: "",
    });
    const [initialData, setInitialData] = useState({});

    const { id } = useParams();
    const location = useLocation();
    const currentUser = location.state?.currentUser || {};

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/users/form/")
            .then((response) => {
                setFormFields(response.data);
                if (isEditMode) {
                    setFormData(currentUser);
                    setInitialData(currentUser);
                }
            })
            .catch((error) => console.error("Error al obtener los datos", error));
    }, [isEditMode, currentUser]);

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const url = isEditMode
            ? `http://localhost:8000/users/form/${id}/`
            : "http://localhost:8000/users/form/";

        const method = isEditMode ? "put" : "post";

        const updatedFields = Object.keys(formData).reduce((acc, key) => {
            if (formData[key] !== initialData[key]) {
                acc[key] = formData[key];
            }
            return acc;
        }, {});

        axios[method](url, updatedFields)
            .then((response) => {
                alert(response.data.message);
                window.location.href = "/";
            })
            .catch((error) => {
                alert("Hubo un error al enviar el formulario.");
                console.error("Error al enviar el formulario", error);
            });
    };

    return (
        <div>
            <h1>{isEditMode ? "Actualizar Usuario" : "Nuevo Usuario"}</h1>
            <form onSubmit={handleSubmit}>
                {formFields &&
                    Object.keys(formFields).map((field) => {
                        const { label, input, type } = formFields[field];

                        return (
                            <div key={field}>
                                <label htmlFor={input.id}>{label}</label>
                                <input
                                    {...input}
                                    value={formData[field] || ""}
                                    onChange={handleInputChange}
                                    name={field}
                                    type={type || "text"}
                                />
                                {field === "password" && (
                                    <div>
                                        <p>Al menos un número.</p>
                                        <p>Al menos una letra mayúscula.</p>
                                        <p>Al menos un carácter especial (!#$%&?).</p>
                                        <p>Mínimo de 8 caracteres en total.</p>
                                    </div>
                                )}
                                <br />
                            </div>
                        );
                    })}
                <button type="submit">{isEditMode ? "Actualizar" : "Enviar"}</button>
            </form>
        </div>
    );
};

export default CustomUserForm;
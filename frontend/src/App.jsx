import React from 'react';
import './App.css';
import { RouterProvider, createBrowserRouter, createRoutesFromElements, Route } from 'react-router-dom';


// Importing User Define Components/Utils.
import Layout from './components/layout/Layout';


// Default Custom React Home Page.
function DefaultReactHome() {
    return (
        <div className="App">
            <h2>
                Welcome! to Django React Boilerplate.
            </h2>
        </div>
    )
}


// Creating All Router and Define All Route.
const router = createBrowserRouter(createRoutesFromElements(
    <Route path='/' element={<Layout />}>
        <Route index element={<DefaultReactHome />} />
    </Route>
))


// Expose the Created Router using RouterProvider (It Comes From react-router-dom).
export default function App() {
    return (
        <RouterProvider router={router} />
    );
}


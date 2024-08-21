// Named Imports.
import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { useDispatch } from 'react-redux';
import { signup } from '../../thunks/signupThunk';

// Default Imports.
import './SignupForm.scss'
import useSignupSelectors from '../../hooks/useSignupSelectors';
import CustomInput from '../customInput/CustomInput';
import Loader from '../../../../components/common/Loader';

export default function SignupForm() {
    const dispatch = useDispatch();

    // Select the auth readux context.
    const { data, status, error } = useSignupSelectors()

    // Define a initial form data for signup.
    const initialFormData = {
        username: '',
        email: '',
        password1: '',
        password2: '',
    }

    // Define a initial form data state.
    const [formData, setFormData] = useState(initialFormData)

    // Handle form data changes.
    function handleFormDataChange(event) {
        const { name, type, checked, value } = event.target
        setFormData((prevFormData) => {
            return {
                ...prevFormData,
                [name]: type === 'checkbox' ? checked : value
            }
        })
    }

    // Handle the form submation.
    function handleFormSubmit(event) {
        event.preventDefault()
        dispatch(signup(formData))
    }

    return (
        <form onSubmit={handleFormSubmit} className='signup-form'>
            <div className='signup-element'>
                {
                    status !== 'succeeded' && (
                        <div className='action-elements'>
                            <h3 className="title">Create your account</h3>
                            <CustomInput
                                type='text'
                                label='username'
                                name='username'
                                onChange={handleFormDataChange}
                                value={formData.username}
                            />
                            {
                                error?.username && (
                                    <h5>{error.username}</h5>
                                )
                            }

                            <CustomInput
                                type='email'
                                label='email'
                                name='email'
                                onChange={handleFormDataChange}
                                value={formData.email}
                            />
                            {
                                error?.email && (
                                    <h5>{error.email}</h5>
                                )
                            }

                            <CustomInput
                                type='password'
                                label='password'
                                name='password1'
                                onChange={handleFormDataChange}
                                value={formData.password1}
                            />
                            {
                                error?.password1 && (
                                    <h5>{error.password1}</h5>
                                )
                            }

                            <CustomInput
                                type='password'
                                label='confirm password'
                                name='password2'
                                onChange={handleFormDataChange}
                                value={formData.password2}
                            />
                            {
                                error?.password2 && (
                                    <h5>{error.password2}</h5>
                                )
                            }

                            {
                                status === 'loading' && (
                                    <div className="signup-btn">
                                        <button type="submit">
                                            <Loader />
                                            <span>loading...</span>
                                        </button>
                                    </div>
                                )
                            }

                            {
                                status !== 'loading' && (
                                    <div className="signup-btn">
                                        <button type="submit">signup</button>
                                    </div>
                                )
                            }
                            <p className='login-text'>
                                have an account?, <Link to="/login">login now</Link>
                            </p>
                        </div>
                    )
                }

                {
                    status === 'succeeded' && (
                        <h3>{data.detail}</h3>
                    )
                }
                
            </div>
        </form>
    )
}

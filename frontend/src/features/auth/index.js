import signinReducer from './slices/signinSlice'
import signoutReducer from './slices/signoutSlice'
import signupReducer from './slices/signupSlice'
import verifyAccountReducer from './slices/verifyAccountSlice'
import resendVerificationKeyReducer from './slices/resendVerificationKeySlice'
import forgotPasswordReducer from './slices/forgotPasswordSlice'
import { refreshAccessTokenThunk } from './thunks/signinThunk'
import { useSigninSelector } from './hooks/useSigninSelector'

// Pages
import LogoutButton from './components/signoutButton/SignoutButton'
import SigninForm from './pages/signinForm/SigninForm'
import SigninFormSkeleton from './pages/signinForm/SigninFormSkeleton'
import ResendVerificationKey from './pages/resendVerificationKey/ResendVerificationKey'
import SignupForm from './pages/signupForm/SignupForm'
import VerifyAccount from './pages/verifyAccount/VerifyAccount'
import ForgotPassword from './pages/forgotPassword/ForgotPassword'
import PasswordResetConfirm from './pages/forgotPassword/PasswordResetConfirm'

export {
  signinReducer,
  signoutReducer,
  signupReducer,
  verifyAccountReducer,
  resendVerificationKeyReducer,
  forgotPasswordReducer,
  refreshAccessTokenThunk,
  useSigninSelector,
  SigninForm,
  SigninFormSkeleton,
  LogoutButton,
  ResendVerificationKey,
  SignupForm,
  VerifyAccount,
  ForgotPassword,
  PasswordResetConfirm,
}

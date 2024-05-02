import * as yup from "yup";

const emailRegex = /[a-z0-9]+@[a-z]+.[a-z]{2,3}/;
const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
const passwordRegex =
  /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;

const allowedDomains = [
  "gmail.com",
  "yahoo.com",
  "outlook.com",
  "aol.com",
  "icloud.com",
  "protonmail.com",
  "yandex.com",
  "zoho.com",
];

const validateEmailDomain = (value?: string) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (value) {
    if (!regex.test(value)) {
      return false; // Invalid email format
    }

    const domain = value.split("@")[1];
    return allowedDomains.includes(domain);
  }
};

export const signupSchema = yup.object().shape({
  firstName: yup.string().required("First Name is required"),
  lastName: yup.string().required("Last Name is required"),
  email: yup
    .string()
    .email()
    .matches(emailRegex, "Email is invalid.")
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  telephone: yup
    .string()
    .matches(phoneRegex, "Invalid phone number")
    .required("Phone number is required"),
  password: yup
    .string()
    .matches(
      passwordRegex,
      "Password must be at least 8 characters and have at least one uppercase, one lowercase, a number and a special characters"
    )
    .required("Password is required"),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref("password")], "Mismatched passwords")
    .required("Please confirm your password"),
  isTeacher: yup.string().oneOf(["true", "false"], "Terms must be accepted").required()
  // terms: yup
  //   .boolean()
  //   .oneOf([true], "Terms must be accepted")
  //   .required("Terms is required"),
});

export const forgotPasswordSchema = yup.object().shape({
  email: yup
    .string()
    .email()
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
});

export const signinSchema = yup.object().shape({
  email: yup
    .string()
    .email()
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  password: yup.string().required(),
});

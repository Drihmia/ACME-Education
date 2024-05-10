import * as yup from "yup";

export const filterSchema = yup.object().shape({
    subject: yup.string(),
    name: yup.string(),
    public: yup.string()
  });
  
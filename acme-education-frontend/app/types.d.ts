export interface cityProps {
  created_at: string;
  id: string;
  name: string;
  state_id: string;
  updated_at: string;
  __class__: string;
}

export interface institutionProps {
  created_at: string;
  id: string;
  name: string;
  city_id: string;
  updated_at: string;
  __class__: string;
}

export interface subjectProps {
  created_at: string;
  id: string;
  name: string;
  updated_at: string;
  __class__: string;
}

export interface siginProps {
  email: string;
  password: string;
  isTeacher: string;
}

export interface User {
  access_token: string;
  user_id: string;
  class: string;
}

export interface UserContext {
  user: User | null;
  updateUser: () => void;
}

export interface lessonFormProps {
  id?: string;
  subject: string;
  subject_id?: string;
  institution?: string;
  institution_id?: string;
  teacher_id?: string;
  teacher?: string;
  name: string;
  download_link: string;
  description: string;
  public: string | boolean;
  class?: string;
  class_id?: string;
  class_alias?: string;
  institutions?: string[]
}


interface responseProps {
  status: string;
  message: string;
}

interface selectedCityProps {
  status: boolean;
  id: string;
}

interface teacherSignupProps {
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  password: string;
  confirm_password: string;
  city: string;
  city_id?: string;
  institution: string;
  institution_id?: string;
  subjects_id?: string[];
  gender: string
  is_teacher: boolean;
}

interface studentSignupProps {
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  password?: string;
  confirm_password?: string;
  city: string;
  city_id?: string;
  institution: string;
  institution_id?: string;
  gender: string;
  class_id?: string;
  class: string;
  teacher_email: string;
  is_teacher: boolean;
  // teacher: string;
}

interface radioProps {
  label: string;
  name: string;
  type: string;
  value: boolean | string;
  checked: boolean
}

interface OtherProps {
  customStyle?: string;
  label: string;
  checkValue?: (val: boolean, id?: string) => void;
  placeholder?: string;
  options?: radioProps[];
  data?: any[];
  optional?: boolean
}

interface searchProps {
  label: string;
  setData: (data: string) => void;
  placeholder: string;
  data: any[];
}

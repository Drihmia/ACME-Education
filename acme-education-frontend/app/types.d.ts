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

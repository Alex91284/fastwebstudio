import { useAuthContext } from "../auth/AuthProvider";

export default function Home() {
  const { token, login, logout } = useAuthContext();

  return (
    <div className="p-6">
      <h2 className="mb-4 text-2xl font-bold">Home Page</h2>
      <p>Token actual: {token || "Ninguno"}</p>
      <button
        className="px-4 py-2 mr-2 text-white bg-green-600"
        onClick={() => login("mi_token_falso")}
      >
        Iniciar sesión
      </button>
      <button
        className="px-4 py-2 text-white bg-red-600"
        onClick={logout}
      >
        Cerrar sesión
      </button>
    </div>
  );
}

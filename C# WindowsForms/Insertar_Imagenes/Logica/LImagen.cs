using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Datos;

namespace Logica
{
    public class LImagen
    {
        public string RecibirImagen(byte[] a)
        {
            DImagen Instancia = new DImagen();
            return Instancia.InsertarImagen(a);
        }
    }
}

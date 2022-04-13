using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Pipes;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestPipeDotNet
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Open the named pipe.
            var server = new NamedPipeServerStream("ik_pipe");

            Console.WriteLine("Waiting for connection...");
            server.WaitForConnection();

            Console.WriteLine("Connected.");
            var reader = new BinaryReader(server);
            var writer = new BinaryWriter(server);

            while (true)
            {
                try
                {
                    // Receive
                    var received_str_length = (int)reader.ReadUInt32();            // Read string length
                    var received_string = new string(reader.ReadChars(received_str_length));    // Read string

                    Console.WriteLine("Received from Python: \"{0}\"", received_string);


                    // Send
                    string tcp_pose = " x y z R P Y ";
                    string message_from_dotnet = string.Format("<tcp_pose>{0}<tcp_pose/>", tcp_pose);

                    var buffer = Encoding.ASCII.GetBytes(received_string);     // Get ASCII byte array     
                    writer.Write((uint)buffer.Length);                // Write string length
                    writer.Write(buffer);                              // Write string
                    Console.WriteLine(".NET sent: \"{0}\"", message_from_dotnet);
                }
                catch (EndOfStreamException)
                {
                    break;                    // When client disconnects
                }
            }

            Console.WriteLine("Client disconnected.");
            server.Close();
            server.Dispose();
        }
    }
}

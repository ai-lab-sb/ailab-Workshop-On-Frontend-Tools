"""
Script de prueba para verificar la conexión con la API del agente de seguros.

Ejecuta este script antes de comenzar a desarrollar tu aplicación Dash
para asegurarte de que la API está funcionando correctamente.

Uso:
    python test_api.py
"""

import requests
import sys

API_URL = "http://localhost:8000"

def test_health():
    """Prueba el endpoint /health"""
    print("=" * 60)
    print("🔍 Probando endpoint /health...")
    print("=" * 60)
    
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Endpoint /health funcionando correctamente")
            print(f"   Status: {data.get('status')}")
            print(f"   Service: {data.get('service')}")
            print(f"   Agent Ready: {data.get('agent_ready')}")
            return True
        else:
            print(f"❌ Error: Status code {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión")
        print("   La API no está corriendo en http://localhost:8000")
        print("   Inicia la API con: cd insurance_agent_api/app && python main.py")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def test_chat():
    """Prueba el endpoint /chat"""
    print("\n" + "=" * 60)
    print("🔍 Probando endpoint /chat...")
    print("=" * 60)
    
    try:
        mensaje = "Hola, ¿qué tipos de seguros ofrecen?"
        print(f"📤 Enviando mensaje: '{mensaje}'")
        
        response = requests.post(
            f"{API_URL}/chat",
            json={
                "message": mensaje,
                "thread_id": "test_dash"
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            respuesta = data.get('response', '')
            print("✅ Endpoint /chat funcionando correctamente")
            print(f"📥 Respuesta del agente:")
            print(f"   {respuesta[:200]}..." if len(respuesta) > 200 else f"   {respuesta}")
            return True
        else:
            print(f"❌ Error: Status code {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Timeout: La API no respondió en 30 segundos")
        print("   Esto puede indicar un problema con tu GOOGLE_API_KEY")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def test_history():
    """Prueba el endpoint /history"""
    print("\n" + "=" * 60)
    print("🔍 Probando endpoint /history...")
    print("=" * 60)
    
    try:
        response = requests.get(f"{API_URL}/history/test_dash", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            history = data.get('history', [])
            print("✅ Endpoint /history funcionando correctamente")
            print(f"   Mensajes en el historial: {len(history)}")
            return True
        else:
            print(f"❌ Error: Status code {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("🧪 Iniciando pruebas de la API del Agente de Seguros")
    print("=" * 60)
    
    # Test 1: Health
    test1_ok = test_health()
    
    if not test1_ok:
        print("\n" + "=" * 60)
        print("⚠️  No se pudo conectar con la API")
        print("=" * 60)
        print("\n📋 Pasos para solucionar:")
        print("1. Asegúrate de estar en la carpeta correcta:")
        print("   cd insurance_agent_api/app")
        print("\n2. Verifica que tengas el archivo .env con tu GOOGLE_API_KEY:")
        print("   cat ../.env")
        print("\n3. Instala las dependencias:")
        print("   pip install -r ../requirements.txt")
        print("\n4. Inicia la API:")
        print("   python main.py")
        print("\n5. En otra terminal, vuelve a ejecutar este script:")
        print("   python test_api.py")
        print("=" * 60)
        sys.exit(1)
    
    # Test 2: Chat
    test2_ok = test_chat()
    
    # Test 3: History
    test3_ok = test_history()
    
    # Resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    print(f"   /health:  {'✅ PASS' if test1_ok else '❌ FAIL'}")
    print(f"   /chat:    {'✅ PASS' if test2_ok else '❌ FAIL'}")
    print(f"   /history: {'✅ PASS' if test3_ok else '❌ FAIL'}")
    print("=" * 60)
    
    if test1_ok and test2_ok and test3_ok:
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("   Estás listo para comenzar a desarrollar tu aplicación Dash.")
        print("\n📝 Siguiente paso:")
        print("   python starter_template.py")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n⚠️  Algunas pruebas fallaron")
        print("   Revisa los errores antes de continuar.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()


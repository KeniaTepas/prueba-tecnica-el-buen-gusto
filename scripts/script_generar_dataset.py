#!/usr/bin/env python3
"""
Script para generar el dataset completo ventas_licorera.csv
Ejecutar: python generar_dataset.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generar_dataset_ventas():
    # Configurar semilla para reproducibilidad
    np.random.seed(42)
    random.seed(42)
    
    # Definir productos y precios base
    productos = {
        'Cerveza': [
            ('Pilsen 330ml', 2.50), ('Club Colombia 330ml', 3.20), ('Aguila 330ml', 2.80),
            ('Stella Artois 330ml', 4.50), ('Corona 355ml', 5.20), ('Heineken 330ml', 4.80),
            ('BBC Cajica 330ml', 6.50), ('Tres Cordilleras IPA 330ml', 7.20)
        ],
        'Licores': [
            ('Aguardiente Antioqueno 750ml', 18.50), ('Ron Medellin 750ml', 22.00),
            ('Whisky Old Parr 750ml', 85.00), ('Vodka Smirnoff 750ml', 32.00),
            ('Ron Bacardi 750ml', 28.50), ('Whisky Buchanans 750ml', 120.00),
            ('Aguardiente Nectar 750ml', 16.80), ('Tequila Jose Cuervo 750ml', 45.00)
        ],
        'Vinos': [
            ('Vino Tinto Gato Negro 750ml', 15.20), ('Vino Blanco Santa Helena 750ml', 12.50),
            ('Vino Rose Marques de Caceres 750ml', 18.00), ('Espumoso Freixenet 750ml', 25.00),
            ('Vino Tinto Casillero del Diablo 750ml', 22.00), ('Vino Blanco Concha y Toro 750ml', 16.50)
        ],
        'Bebidas_Preparadas': [
            ('Smirnoff Ice 275ml', 4.20), ('Four Loko 473ml', 6.80),
            ('Bacardi Breezer 275ml', 4.50), ('Mikes Hard 355ml', 5.50)
        ]
    }
    
    # Definir sucursales y zonas
    sucursales_zona = {
        1: 'Norte', 2: 'Norte', 3: 'Norte',
        4: 'Sur', 5: 'Sur', 6: 'Sur', 
        7: 'Este', 8: 'Este', 9: 'Este',
        10: 'Oeste', 11: 'Oeste', 12: 'Oeste',
        13: 'Centro', 14: 'Centro', 15: 'Centro'
    }
    
    # Eventos especiales con fechas aproximadas
    eventos_especiales = {
        'Año_Nuevo': [(1, 1), (12, 31)],
        'San_Valentin': [(2, 14)],
        'Dia_Padre': [(3, 19), (6, 19)],  # Marzo en algunos países, Junio en otros
        'Pascua': [(4, 17), (4, 9), (3, 31)],  # Varía cada año
        'Dia_Madre': [(5, 8), (5, 14)],  # Segunda semana de mayo
        'Halloween': [(10, 31)],
        'Navidad': [(12, 24), (12, 25)]
    }
    
    # Crear rango de fechas
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    datos = []
    
    print(f"Generando datos para {len(date_range)} días...")
    
    for fecha in date_range:
        # Determinar si es evento especial
        evento = 'Ninguno'
        for evento_nombre, fechas_evento in eventos_especiales.items():
            for mes_evento, dia_evento in fechas_evento:
                if fecha.month == mes_evento and fecha.day == dia_evento:
                    evento = evento_nombre
                    break
        
        # Factores de estacionalidad
        # Más ventas en fines de semana (viernes=5, sábado=6)
        factor_dia_semana = 1.0
        if fecha.weekday() == 4:  # Viernes
            factor_dia_semana = 1.4
        elif fecha.weekday() == 5:  # Sábado  
            factor_dia_semana = 1.6
        elif fecha.weekday() == 6:  # Domingo
            factor_dia_semana = 1.2
        
        # Más ventas en diciembre y eventos especiales
        factor_mes = 1.0
        if fecha.month == 12:  # Diciembre
            factor_mes = 1.5
        elif fecha.month in [6, 7, 8]:  # Vacaciones mitad de año
            factor_mes = 1.2
        
        # Factor evento especial
        factor_evento = 2.0 if evento != 'Ninguno' else 1.0
        
        # Temperatura simulada (Colombia)
        temp_base = 24  # Temperatura promedio en Colombia
        variacion_mes = 3 * np.sin(2 * np.pi * fecha.month / 12)
        temperatura = temp_base + variacion_mes + np.random.normal(0, 2)
        
        # Lluvia (más probable en abril-mayo y octubre-noviembre)
        prob_lluvia = 0.1
        if fecha.month in [4, 5, 10, 11]:
            prob_lluvia = 0.4
        lluvia = 1 if np.random.random() < prob_lluvia else 0
        
        # Generar ventas para cada sucursal
        for sucursal_id in range(1, 16):
            zona = sucursales_zona[sucursal_id]
            
            # Factor zona (Centro vende más)
            factor_zona = 1.0
            if zona == 'Centro':
                factor_zona = 1.3
            elif zona == 'Norte':
                factor_zona = 1.1
            
            # Número de productos vendidos por día por sucursal
            num_ventas = np.random.poisson(8 * factor_dia_semana * factor_mes * factor_evento * factor_zona)
            num_ventas = max(1, min(num_ventas, 25))  # Entre 1 y 25 ventas por día
            
            productos_vendidos = []
            for _ in range(num_ventas):
                # Seleccionar categoría (cervezas más populares)
                categoria_probs = {
                    'Cerveza': 0.5,
                    'Licores': 0.25, 
                    'Vinos': 0.15,
                    'Bebidas_Preparadas': 0.1
                }
                categoria = np.random.choice(list(categoria_probs.keys()), 
                                           p=list(categoria_probs.values()))
                
                # Seleccionar producto de la categoría
                producto_info = random.choice(productos[categoria])
                nombre_producto, precio_base = producto_info
                
                # Ajustar precio por inflación anual (~5%)
                anos_desde_2022 = fecha.year - 2022
                precio_unitario = precio_base * (1.05 ** anos_desde_2022)
                precio_unitario = round(precio_unitario, 2)
                
                # Cantidad vendida (influenciada por precio y eventos)
                if categoria == 'Cerveza':
                    cantidad_base = np.random.poisson(15)
                elif categoria == 'Licores':
                    cantidad_base = np.random.poisson(5)
                elif categoria == 'Vinos':
                    cantidad_base = np.random.poisson(7)
                else:  # Bebidas preparadas
                    cantidad_base = np.random.poisson(10)
                
                # Ajustar por factores
                cantidad_vendida = max(1, int(cantidad_base * factor_evento * 
                                             (1.2 if temperatura > 28 else 1.0)))
                
                # Promociones (20% de probabilidad, mayor en eventos)
                prob_promocion = 0.3 if evento != 'Ninguno' else 0.15
                promocion_activa = 1 if np.random.random() < prob_promocion else 0
                
                total_venta = precio_unitario * cantidad_vendida
                
                # Crear registro
                registro = {
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'sucursal_id': sucursal_id,
                    'categoria_producto': categoria,
                    'nombre_producto': nombre_producto,
                    'precio_unitario': precio_unitario,
                    'cantidad_vendida': cantidad_vendida,
                    'total_venta': round(total_venta, 2),
                    'dia_semana': fecha.weekday() + 1,  # 1=Lunes, 7=Domingo
                    'mes': fecha.month,
                    'promocion_activa': promocion_activa,
                    'evento_especial': evento,
                    'temperatura_promedio': round(temperatura, 1),
                    'lluvia': lluvia,
                    'zona_sucursal': zona
                }
                
                datos.append(registro)
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    # Ordenar por fecha y sucursal
    df = df.sort_values(['fecha', 'sucursal_id']).reset_index(drop=True)
    
    print(f"Dataset generado con {len(df)} registros")
    print(f"Período: {df['fecha'].min()} a {df['fecha'].max()}")
    print(f"Sucursales: {df['sucursal_id'].nunique()}")
    print(f"Productos únicos: {df['nombre_producto'].nunique()}")
    print(f"Ventas totales: ${df['total_venta'].sum():,.2f}")
    
    return df

def main():
    """Función principal"""
    print("=== Generador de Dataset: Ventas Licorera ===")
    
    # Generar dataset
    df = generar_dataset_ventas()
    
    # Guardar archivo
    filename = '../data/ventas_licorera.csv'
    df.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"\n✅ Dataset guardado como: {filename}")
    print(f"📊 Tamaño del archivo: {len(df)} filas x {len(df.columns)} columnas")
    
    # Mostrar estadísticas básicas
    print("\n📈 Estadísticas básicas:")
    print(f"   • Ventas por día promedio: {len(df) / 1095:.1f}")
    print(f"   • Ticket promedio: ${df['total_venta'].mean():.2f}")
    print(f"   • Venta máxima: ${df['total_venta'].max():.2f}")
    print(f"   • Categorías: {', '.join(df['categoria_producto'].unique())}")
    
    print("\n🎯 Dataset listo para la prueba técnica!")

if __name__ == "__main__":
    main()
